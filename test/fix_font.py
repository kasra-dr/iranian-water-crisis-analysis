import matplotlib
import os

try:
    # Find the cache directory
    cache_dir = matplotlib.get_cachedir()
    print(f"Matplotlib cache directory is: {cache_dir}")

    # Find the font cache file
    font_cache_file = os.path.join(cache_dir, 'fontlist-v330.json') # The version number might differ
    
    # Try to find the file regardless of version
    cache_files = [f for f in os.listdir(cache_dir) if f.startswith('fontlist-') and f.endswith('.json')]

    if not cache_files:
        print("No font cache file found to delete.")
    else:
        for f in cache_files:
            file_path = os.path.join(cache_dir, f)
            try:
                os.remove(file_path)
                print(f"Successfully deleted font cache file: {f}")
            except OSError as e:
                print(f"Error deleting file {f}: {e}")

    print("\nFont cache cleared. Please re-run your plotting script.")
    print("Matplotlib will rebuild the cache, which may take a moment.")

except Exception as e:
    print(f"An error occurred: {e}")