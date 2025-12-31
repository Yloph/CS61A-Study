### Sound


from wave import open
from struct import Struct
from math import floor 

frame_rate = 11025
c_freq, e_freq, g_freq = 261.63, 329.63, 392.0

def encode(x):
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name = "song.wav", seconds = 2):
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1
    
    out.close()

def tri(frequency, amplitude = 0.3):
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    
    return sampler

def both(f, g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade = 0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
        
    return sampler

def mario(n1, n2, n3, n4):
    t = 0
    song = note(n2, t, t + 1/8)
    t += 1/8
    song = both(song, note(n2, t, t + 1/8))
    t += 1/4
    song = both(song, note(n2, t, t + 1/8))
    t += 1/4
    song = both(song, note(n1, t, t + 1/8))
    t += 1/8
    song = both(song, note(n2, t, t + 1/8))
    t += 1/4
    song = both(song, note(n3, t, t + 1/4))
    t += 1/2
    song = both(song, note(n4, t, t + 1/4))
    t += 1/2

    return song

def mario_at(ocwave):
    c, e = tri(ocwave * c_freq), tri(ocwave * e_freq)
    g, low_g = tri(ocwave * g_freq), tri(ocwave * g_freq / 2)
    return mario(c, e, g, low_g)

play(both(mario_at(1), mario_at(3/2)))