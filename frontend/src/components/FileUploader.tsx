import React, { useState, useCallback } from 'react';
import { convertFile } from '../api/client';

export const FileUploader = () => {
  const [isDragging, setIsDragging] = useState(false);
  const [status, setStatus] = useState<'idle' | 'converting' | 'success' | 'error'>('idle');
  const [errorMessage, setErrorMessage] = useState('');
  const [downloadLink, setDownloadLink] = useState<{ url: string; filename: string } | null>(null);
  const progressSteps = ['Upload', 'Convert', 'Package'];

  const handleDrag = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setIsDragging(true);
    } else if (e.type === 'dragleave') {
      setIsDragging(false);
    }
  }, []);

  const processFile = async (file: File) => {
    setStatus('converting');
    setErrorMessage('');
    setDownloadLink(null);

    // GA4 Event: File Upload Started
    if (typeof window !== 'undefined' && (window as any).gtag) {
      (window as any).gtag('event', 'file_upload', {
        file_type: file.type,
        file_size: file.size,
        file_name: file.name.split('.').pop() // extension only
      });
    }

    try {
      const result = await convertFile(file);
      setStatus('success');
      setDownloadLink(result);

      // GA4 Event: Conversion Success
      if (typeof window !== 'undefined' && (window as any).gtag) {
        (window as any).gtag('event', 'conversion_success', {
          file_type: file.type,
          output_filename: result.filename
        });
      }
    } catch (error) {
      setStatus('error');
      setErrorMessage(error instanceof Error ? error.message : 'Unknown error');

      // GA4 Event: Conversion Error
      if (typeof window !== 'undefined' && (window as any).gtag) {
        (window as any).gtag('event', 'conversion_error', {
          error_message: error instanceof Error ? error.message : 'Unknown error',
          file_type: file.type
        });
      }
    }
  };

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    const files = e.dataTransfer.files;
    if (files?.[0]) processFile(files[0]);
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) processFile(e.target.files[0]);
  };

  const reset = () => {
    setStatus('idle');
    setDownloadLink(null);
    setErrorMessage('');
  };

  return (
    <div className="w-full">
      {status === 'idle' && (
        <div
          className={`upload-zone ${isDragging ? 'dragging' : ''}`}
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
        >
          <label className="flex flex-col items-center cursor-pointer">
            <div className="w-6 h-6 mb-1 rounded-full bg-gradient-to-br from-blue-100 to-purple-100 dark:from-blue-900/30 dark:to-purple-900/30 flex items-center justify-center">
              <svg className="w-3 h-3 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
            </div>
            <p className="text-xs font-medium">Drop file or click</p>
            <span className="text-xs text-slate-400">JPG, PNG, DOC, DOCX (10MB max)</span>
            <input type="file" className="hidden" onChange={handleChange} accept=".jpg,.jpeg,.png,.doc,.docx" />
          </label>
          <div className="limit-row">
            <span>Max 10MB</span>
            <span>PDF output</span>
          </div>
        </div>
      )}

      {status === 'converting' && (
        <div className="glass-card p-4 text-center">
          <div className="w-6 h-6 mx-auto mb-2 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center">
            <svg className="w-3 h-3 text-blue-500 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
            </svg>
          </div>
          <p className="text-xs font-medium">Converting...</p>
          <div className="progress-list">
            {progressSteps.map((step, index) => (
              <div key={step} className="progress-row">
                <span className="progress-label">{step}</span>
                <div className="progress-track">
                  <div className={`progress-bar progress-bar-${index + 1}`} />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {status === 'success' && (
        <div className="glass-card p-4 text-center">
          <div className="w-6 h-6 mx-auto mb-2 rounded-full bg-green-100 dark:bg-green-900/30 flex items-center justify-center">
            <svg className="w-3 h-3 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <p className="text-xs font-medium mb-1">Success!</p>
          <p className="text-[10px] text-slate-500 mb-4 truncate px-4">
            {downloadLink?.filename}
          </p>
          {downloadLink && (
            <a
              href={downloadLink.url}
              download={downloadLink.filename}
              className="btn-primary inline-flex items-center gap-2"
              onClick={() => {
                // GA4 Event: File Download
                if (typeof window !== 'undefined' && (window as any).gtag) {
                  (window as any).gtag('event', 'file_download', {
                    file_name: downloadLink.filename
                  });
                }
              }}
            >
              <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              Download PDF
            </a>
          )}
          <button onClick={reset} className="block mx-auto mt-2 text-xs text-slate-400 hover:text-slate-600 dark:hover:text-slate-300">
            Convert another
          </button>
        </div>
      )}

      {status === 'error' && (
        <div className="glass-card p-4 text-center">
          <div className="w-6 h-6 mx-auto mb-2 rounded-full bg-red-100 dark:bg-red-900/30 flex items-center justify-center">
            <svg className="w-3 h-3 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
          <p className="text-xs font-medium text-red-500 mb-1">Error</p>
          <p className="text-xs text-slate-400 mb-2">{errorMessage}</p>
          <button onClick={reset} className="btn-primary">Try again</button>
        </div>
      )}
    </div>
  );
};
