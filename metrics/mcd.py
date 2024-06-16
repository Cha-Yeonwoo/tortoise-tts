from pymcd.mcd import Calculate_MCD

# instance of MCD class
# three different modes "plain", "dtw" and "dtw_sl" for the above three MCD metrics 
mcd_toolbox = Calculate_MCD(MCD_mode="dtw")

# two inputs w.r.t. reference (ground-truth) and synthesized speeches, respectively
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/steve_jobs_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/steve_jobs_mos_ultra_fast.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/steve_jobs_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/steve_jobs_mos_fast.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/steve_jobs_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/steve_jobs_mos_standard.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/donald_trump_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/donald_trump_mos_ultra_fast.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/donald_trump_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/donald_trump_mos_fast.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/donald_trump_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/donald_trump_mos_standard.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/elon_musk_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/elon_musk_mos_ultra_fast.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/elon_musk_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/elon_musk_mos_fast.wav")
print(mcd_value)
mcd_value = mcd_toolbox.calculate_mcd("/mnt/disk1/ivymm02/tortoise-tts/ground_truth/elon_musk_mos_gt.wav", "/mnt/disk1/ivymm02/tortoise-tts/generated_output/elon_musk_mos_standard.wav")
print(mcd_value)
