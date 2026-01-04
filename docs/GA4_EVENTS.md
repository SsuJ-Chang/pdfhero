# GA4 事件追蹤配置文檔

## 📊 已追蹤的事件

我們已經在應用中設定了以下自定義事件追蹤：

### 1. **file_upload** - 檔案上傳
**觸發時機**：用戶選擇或拖放檔案時

**參數**：
- `file_type`: 檔案 MIME 類型（如 `image/png`, `application/msword`）
- `file_size`: 檔案大小（bytes）
- `file_name`: 檔案副檔名（如 `png`, `docx`）

### 2. **conversion_success** - 轉換成功
**觸發時機**：PDF 轉換成功完成時

**參數**：
- `file_type`: 原始檔案類型
- `output_filename`: 輸出的 PDF 檔名

### 3. **conversion_error** - 轉換失敗
**觸發時機**：轉換過程中發生錯誤時

**參數**：
- `error_message`: 錯誤訊息
- `file_type`: 原始檔案類型

### 4. **pdf_download** - PDF 下載
**觸發時機**：用戶點擊「Download PDF」按鈕時

**參數**：
- `filename`: 下載的 PDF 檔名

---

## 🔍 如何在 GA4 後台查看事件

### 方法 1：即時總覽
1. GA4 後台 → 左側「報表」→「即時」
2. 下方的「依事件名稱劃分使用者」區塊
3. 應該會看到 `file_upload`, `conversion_success`, `pdf_download` 等事件

### 方法 2：事件報表
1. GA4 後台 → 左側「報表」→「參與」→「事件」
2. 點擊任一事件名稱（如 `conversion_success`）
3. 可看到該事件的詳細參數與計數

### 方法 3：建立自訂報表（進階）
```
1. 左側「探索」→ 建立新的探索
2. 選擇「自由格式」
3. 維度：新增「事件名稱」、「檔案類型」等
4. 指標：新增「事件計數」
5. 設定視覺化方式（表格、圖表等）
```

---

## 📈 常用分析範例

### 轉換成功率
```
轉換成功率 = conversion_success 事件數 / file_upload 事件數 × 100%
```

### 最常轉換的檔案類型
1. 進入「事件」報表 → 點選 `file_upload`
2. 查看「file_type」參數的分布

### 錯誤率與原因
1. 進入「事件」報表 → 點選 `conversion_error`
2. 查看「error_message」參數
3. 分析常見錯誤並改進

---

## 🎯 建議的追蹤目標

您可以在 GA4 設定「轉換」目標：

1. **主要轉換**：`conversion_success`（成功轉換）
2. **次要轉換**：`pdf_download`（實際下載）

**設定方法**：
```
1. GA4 後台 → 管理（左下）→ 事件（資源欄）
2. 找到 `conversion_success`
3. 開啟「標示為轉換」
```

這樣您就可以在「轉換」報表中看到這些關鍵指標了！
