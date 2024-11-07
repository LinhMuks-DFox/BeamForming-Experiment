import numpy as np
from scipy.io import wavfile
from scipy.signal import resample

# 参数设置
mic_distance = 0.2  # 麦克风间距（米）
angle = np.radians(45)  # 假设声源角度为45度（可以更改）
temperature = 20  # 气温（摄氏度）
sound_speed = 331.5 + 0.61 * temperature  # 计算声速（米/秒）

# 计算延迟时间
delay_time = mic_distance * np.cos(angle) / sound_speed  # 延迟时间（秒）

# 读取音频文件（假设两个音轨文件为mic1.wav和mic2.wav）
sample_rate1, mic1_signal = wavfile.read("mic1.wav")
sample_rate2, mic2_signal = wavfile.read("mic2.wav")

# 确保采样率一致
assert sample_rate1 == sample_rate2, "两个音频文件的采样率不一致"
sample_rate = sample_rate1

# 将延迟时间转换为样本数
delay_samples = int(delay_time * sample_rate)

# 对麦克风2的信号进行延迟
mic2_signal_delayed = np.pad(mic2_signal, (delay_samples, 0), 'constant')[:len(mic1_signal)]

# 叠加信号，实现波束形成
beamformed_signal = mic1_signal + mic2_signal_delayed

# 输出波束形成后的音频
wavfile.write("beamformed_output.wav", sample_rate, beamformed_signal.astype(np.int16))

print("波束形成处理完成，已输出文件 'beamformed_output.wav'")
