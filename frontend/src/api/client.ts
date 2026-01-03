export interface ConvertResponse {
  path: string;
  filename: string;
  format: string;
  size: number;
  content_type: string;
}

export async function convertFile(file: File): Promise<{ url: string; filename: string }> {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("/api/convert", {
    method: "POST",
    body: formData,
  });

  // Safety check: Ensure we got a PDF
  const contentType = response.headers.get('Content-Type');
  if (!contentType || !contentType.includes('application/pdf')) {
    const text = await response.text();
    throw new Error(`Expected PDF but received: ${contentType}. Body: ${text.substring(0, 100)}`);
  }

  const blob = await response.blob();
  const contentDisposition = response.headers.get('Content-Disposition');
  let filename = file.name.replace(/\.[^/.]+$/, "") + ".pdf";

  if (contentDisposition) {
    // Robust parsing for both filename and filename*
    const filenameMatch = contentDisposition.match(/filename="?([^";\n]+)"?/i);
    const filenameStarMatch = contentDisposition.match(/filename\*=utf-8''([^";\n]+)/i);

    if (filenameStarMatch && filenameStarMatch[1]) {
      filename = decodeURIComponent(filenameStarMatch[1]);
    } else if (filenameMatch && filenameMatch[1]) {
      filename = filenameMatch[1];
    }
  }

  const url = window.URL.createObjectURL(blob);
  return { url, filename };
}
