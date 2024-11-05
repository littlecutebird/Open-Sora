resolution = "720p"
aspect_ratio = "9:16"
num_frames = "4s"
fps = 24
frame_interval = 1
save_fps = 24
save_dir = "./samples/longnn/"
seed = 42
batch_size = 1
multi_resolution = "STDiT2"
dtype = "fp16" #"bf16"
condition_frame_length = 5
align = 5
model = dict(
    type="STDiT3-XL/2",
    from_pretrained="hpcai-tech/OpenSora-STDiT-v3",
    qk_norm=True,
    enable_flash_attn=True,
    enable_layernorm_kernel=True,
)
vae = dict(
    type="OpenSoraVAE_V1_2",
    from_pretrained="hpcai-tech/OpenSora-VAE-v1.2",
    micro_frame_size=17,
    micro_batch_size=4,
)
text_encoder = dict(
    type="t5",
    from_pretrained="DeepFloyd/t5-v1_1-xxl",
    model_max_length=300,
)
scheduler = dict(
    type="rflow",
    use_timestep_transform=True,
    num_sampling_steps=30,
    cfg_scale=7.0,
)
aes = 6.5
flow = None

prompt_path="./configs/opensora-v1-2/inference/sample_prompts.txt"
# prompt=["A day in the life of a busy city street from dawn to dusk.", "A timelapse of a flower blooming in a garden.", "An animation of a spaceship traveling through a colorful galaxy."]