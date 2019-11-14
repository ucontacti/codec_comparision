# In[1]: Header
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


# In[2]: data loading
df = pd.read_csv("stream/2/MJPEG.csv")
df['Time in millisecond'] /= 1000000000
# df['Data Size'].head()
# df['Time in millisecond'].head()
lb = "MJPEG | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'r', label= lb, alpha=0.8)

# %%
df = pd.read_csv("stream/2/VP8.csv")
df['Time in millisecond'] /= 1000000000

# df['Data Size'].head()
# df['Time in millisecond'].head()

lb = "VP8 | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'b', label= lb, alpha=0.8)


# %%
df = pd.read_csv("stream/2/H264.csv")
df['Time in millisecond'] /= 1000000000

# df['Data Size'].head()
# df['Time in millisecond'].head()

lb = "H264 | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'y', label= lb, alpha=0.8)


# %%
df = pd.read_csv("stream/2/VP9.csv")
df['Time in millisecond'] /= 1000000000

# df['Data Size'].head()
# df['Time in millisecond'].head()

lb = "VP9 | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'g', label= lb, alpha=0.8)
plt.legend(loc='best')
plt.xlabel('Time (seconds)')
plt.ylabel('Size (bit)')
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.show()


# %%
df = pd.read_csv("image/2/bitmap.csv")
df['Time in millisecond'] /= 1000000000

df['Data Size'].head()
# df['Time in millisecond'].head()

lb = "Bitmap | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'r', label= lb, alpha=0.8)


# %%
df = pd.read_csv("image/2/lz_rgb.csv")
df['Time in millisecond'] /= 1000000000

df['Data Size'].head()
# df['Time in millisecond'].head()

lb = "LZ_RGB | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'g', label= lb, alpha=0.8)


# %%
df = pd.read_csv("image/2/lz_4.csv")
df['Time in millisecond'] /= 1000000000

df['Data Size'].head()
# df['Time in millisecond'].head()

lb = "LZ_4 | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'b', label= lb, alpha=0.8)



# %%
df = pd.read_csv("image/2/quic.csv")
df['Time in millisecond'] /= 1000000000

df['Data Size'].head()
# df['Time in millisecond'].head()

lb = "QUIC | Sum: " + ('%.1f' % (df['Data Size'].sum()/ 1024 / 8 )) + " KB | Mean: " + ('%.1f' % (df['Data Size'].mean()/ 1024 / 8 )) + " KB"
plt.plot(df['Time in millisecond'], df['Data Size'], 'y', label= lb, alpha=0.8)
plt.legend(loc='best')
plt.xlabel('Time (seconds)')
plt.ylabel('Size (bit)')
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.show()


# %%
