
from isaacsim.asset.importer.urdf import _urdf
import omni.kit.commands
from omni.isaac.core import World



urdf_path = r"G:\isaacsim\Stewart\Stewart\URDF\Stewart.urdf"
urdf_name = "Stewart.urdf"



def setup():
    # Get the world object to set up the simulation environment
    world = World()

    # Add a default ground plane to the scene for the robot to interact with
    world.scene.add_default_ground_plane()

    return world
'''
    # Acquire the URDF extension interface for parsing and importing URDF files
    urdf_interface = _urdf.acquire_urdf_interface()

    # Configure the settings for importing the URDF file
    import_config = _urdf.ImportConfig()
    import_config.convex_decomp = False  # Disable convex decomposition for simplicity
    import_config.fix_base = False       # DO NOT Fix the base of the robot to the ground
    import_config.make_default_prim = True  # Make the robot the default prim in the scene
    import_config.self_collision = False  # Disable self-collision for performance
    import_config.distance_scale = 1     # Set distance scale for the robot
    import_config.density = 0.0          # Set density to 0 (use default values)

    # Retrieve the path of the URDF file from the extension


    # Parse the robot's URDF file to generate a robot model
    result, robot_model = omni.kit.commands.execute(
        "URDFParseFile",
        urdf_path = urdf_path,
        import_config=import_config
    )

    # Update the joint drive parameters for better stiffness and damping
    for joint in robot_model.joints:
        robot_model.joints[joint].drive.strength = 1047.19751  # High stiffness value
        robot_model.joints[joint].drive.damping = 52.35988    # Moderate damping value

    # Import the robot onto the current stage and retrieve its prim path
    result, prim_path = omni.kit.commands.execute(
        "URDFImportRobot",
        urdf_robot=robot_model,
        import_config=import_config,
    )
'''
    

