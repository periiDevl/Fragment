import pygltflib

def obj_to_gltf(input_obj_path, output_gltf_path):
    """Converts an OBJ file to a GLTF file.

    Args:
        input_obj_path (str): Path to the input OBJ file.
        output_gltf_path (str): Path to the output GLTF file.
    """

    gltf_data = pygltflib.load_gltf(input_obj_path)
    pygltflib.save_gltf(gltf_data, output_gltf_path)

# Example usage
input_obj_path = "path/to/your/model.obj"
output_gltf_path = "path/to/output.gltf"
obj_to_gltf(input_obj_path, output_gltf_path)
