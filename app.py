import webview
import os
import sys
from pypdf import PdfWriter, PdfReader


def resource_path(relative):
    """Works both when running normally and when frozen by PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative)


class API:
    def merge_pdfs(self, file_paths, output_path):
        try:
            if not file_paths:
                return {"success": False, "error": "No files selected."}

            if not output_path:
                return {"success": False, "error": "No save location selected."}

            if not output_path.lower().endswith(".pdf"):
                output_path += ".pdf"

            writer = PdfWriter()
            for path in file_paths:
                reader = PdfReader(path)
                for page in reader.pages:
                    writer.add_page(page)

            with open(output_path, "wb") as f:
                writer.write(f)

            return {"success": True, "output_path": output_path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def open_save_dialog(self, suggested_name):
        result = window.create_file_dialog(
            webview.SAVE_DIALOG,
            save_filename=suggested_name if suggested_name else "merged.pdf",
            file_types=("PDF Files (*.pdf)",)
        )
        if not result:
            return None
        return result[0] if isinstance(result, (list, tuple)) else result

    def open_file_dialog(self):
        result = window.create_file_dialog(
            webview.OPEN_DIALOG,
            allow_multiple=True,
            file_types=("PDF Files (*.pdf)",)
        )
        if result:
            files = []
            for path in result:
                files.append({
                    "path": path,
                    "name": os.path.basename(path),
                    "size": self._format_size(os.path.getsize(path))
                })
            return files
        return []

    def _format_size(self, size_bytes):
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f} MB"


api = API()

with open(resource_path("index.html"), "r") as f:
    html = f.read()

window = webview.create_window(
    "PDF Merger",
    html=html,
    js_api=api,
    width=700,
    height=620,
    resizable=True,
    min_size=(500, 500),
    background_color="#0f0f0f"
)

webview.start(debug=False)