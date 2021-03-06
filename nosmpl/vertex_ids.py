from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

# Joint name to vertex mapping. SMPL/SMPL-H/SMPL-X vertices that correspond to
# MSCOCO and OpenPose joints
vertex_ids = {
    "smplh": {
        "nose": 332,
        "reye": 6260,
        "leye": 2800,
        "rear": 4071,
        "lear": 583,
        "rthumb": 6191,
        "rindex": 5782,
        "rmiddle": 5905,
        "rring": 6016,
        "rpinky": 6133,
        "lthumb": 2746,
        "lindex": 2319,
        "lmiddle": 2445,
        "lring": 2556,
        "lpinky": 2673,
        "LBigToe": 3216,
        "LSmallToe": 3226,
        "LHeel": 3387,
        "RBigToe": 6617,
        "RSmallToe": 6624,
        "RHeel": 6787,
    },
    "smplx": {
        "nose": 9120,
        "reye": 9929,
        "leye": 9448,
        "rear": 616,
        "lear": 6,
        "rthumb": 8079,
        "rindex": 7669,
        "rmiddle": 7794,
        "rring": 7905,
        "rpinky": 8022,
        "lthumb": 5361,
        "lindex": 4933,
        "lmiddle": 5058,
        "lring": 5169,
        "lpinky": 5286,
        "LBigToe": 5770,
        "LSmallToe": 5780,
        "LHeel": 8846,
        "RBigToe": 8463,
        "RSmallToe": 8474,
        "RHeel": 8635,
    },
    "mano": {
        "thumb": 744,
        "index": 320,
        "middle": 443,
        "ring": 554,
        "pinky": 671,
    },
}


JOINT_MAP = {
    "OP Nose": 24,
    "OP Neck": 12,
    "OP RShoulder": 17,
    "OP RElbow": 19,
    "OP RWrist": 21,
    "OP LShoulder": 16,
    "OP LElbow": 18,
    "OP LWrist": 20,
    "OP MidHip": 0,
    "OP RHip": 2,
    "OP RKnee": 5,
    "OP RAnkle": 8,
    "OP LHip": 1,
    "OP LKnee": 4,
    "OP LAnkle": 7,
    "OP REye": 25,
    "OP LEye": 26,
    "OP REar": 27,
    "OP LEar": 28,
    "OP LBigToe": 29,
    "OP LSmallToe": 30,
    "OP LHeel": 31,
    "OP RBigToe": 32,
    "OP RSmallToe": 33,
    "OP RHeel": 34,
    "Right Ankle": 8,
    "Right Knee": 5,
    "Right Hip": 45,
    "Left Hip": 46,
    "Left Knee": 4,
    "Left Ankle": 7,
    "Right Wrist": 21,
    "Right Elbow": 19,
    "Right Shoulder": 17,
    "Left Shoulder": 16,
    "Left Elbow": 18,
    "Left Wrist": 20,
    "Neck (LSP)": 47,
    "Top of Head (LSP)": 48,
    "Pelvis (MPII)": 49,
    "Thorax (MPII)": 50,
    "Spine (H36M)": 51,
    "Jaw (H36M)": 52,
    "Head (H36M)": 53,
    "Nose": 24,
    "Left Eye": 26,
    "Right Eye": 25,
    "Left Ear": 28,
    "Right Ear": 27,
}
JOINT_NAMES = [
    "OP Nose",
    "OP Neck",
    "OP RShoulder",
    "OP RElbow",
    "OP RWrist",
    "OP LShoulder",
    "OP LElbow",
    "OP LWrist",
    "OP MidHip",
    "OP RHip",
    "OP RKnee",
    "OP RAnkle",
    "OP LHip",
    "OP LKnee",
    "OP LAnkle",
    "OP REye",
    "OP LEye",
    "OP REar",
    "OP LEar",
    "OP LBigToe",
    "OP LSmallToe",
    "OP LHeel",
    "OP RBigToe",
    "OP RSmallToe",
    "OP RHeel",
    "Right Ankle",
    "Right Knee",
    "Right Hip",
    "Left Hip",
    "Left Knee",
    "Left Ankle",
    "Right Wrist",
    "Right Elbow",
    "Right Shoulder",
    "Left Shoulder",
    "Left Elbow",
    "Left Wrist",
    "Neck (LSP)",
    "Top of Head (LSP)",
    "Pelvis (MPII)",
    "Thorax (MPII)",
    "Spine (H36M)",
    "Jaw (H36M)",
    "Head (H36M)",
    "Nose",
    "Left Eye",
    "Right Eye",
    "Left Ear",
    "Right Ear",
]
JOINT_NAMES_OPENPOSE25_ONLY_MAP = {
    "OP Nose": 24,
    "OP Neck": 12,
    "OP RShoulder": 17,
    "OP RElbow": 19,
    "OP RWrist": 21,
    "OP LShoulder": 16,
    "OP LElbow": 18,
    "OP LWrist": 20,
    "OP MidHip": 0,
    "OP RHip": 2,
    "OP RKnee": 5,
    "OP RAnkle": 8,
    "OP LHip": 1,
    "OP LKnee": 4,
    "OP LAnkle": 7,
    "OP REye": 25,
    "OP LEye": 26,
    "OP REar": 27,
    "OP LEar": 28,
    "OP LBigToe": 29,
    "OP LSmallToe": 30,
    "OP LHeel": 31,
    "OP RBigToe": 32,
    "OP RSmallToe": 33,
    "OP RHeel": 34,
}

JOINT_IDS = {JOINT_NAMES[i]: i for i in range(len(JOINT_NAMES))}
H36M_TO_J17 = [6, 5, 4, 1, 2, 3, 16, 15, 14, 11, 12, 13, 8, 10, 0, 7, 9]
H36M_TO_J14 = H36M_TO_J17[:14]
