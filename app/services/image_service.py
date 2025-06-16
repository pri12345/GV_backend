import os
from werkzeug.utils import secure_filename
from datetime import datetime

class ImageService:
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ImageService.ALLOWED_EXTENSIONS
    
    @staticmethod
    def save_image(file, item_id):
        if file and ImageService.allowed_file(file.filename):
            # Create a secure filename
            filename = secure_filename(file.filename)
            
            # Create a unique filename using timestamp and item_id
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            unique_filename = f"{item_id}_{timestamp}_{filename}"
            
            # Ensure the upload directory exists
            upload_dir = os.path.join('app', 'static', 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            
            # Save the file
            file_path = os.path.join(upload_dir, unique_filename)
            file.save(file_path)
            
            # Return the relative path for database storage
            return f"uploads/{unique_filename}"
        
        return None 