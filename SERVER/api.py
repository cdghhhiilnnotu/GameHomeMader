my_dict = {
    "game0": {
      "demo_file": "gta6_demo.zip", 
      "id": 1, 
      "videos": "gta6_videos.mp4"
    }, 
    "game1": {
      "demo_file": "botw2_demo.zip", 
      "id": 2, 
      "videos": "botw2_videos.mp4"
    }, 
    "game2": {
      "demo_file": "gowr_demo.zip", 
      "id": 3, 
      "videos": "gowr_videos.mp4"
    }
}

target_id = 3

# Iterate through the dictionary
for key, value in my_dict.items():
    if value["id"] == target_id:
        print(f'Element with id = {target_id}: {key} - {value}')