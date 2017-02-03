import numpy as np
if __name__ == "__main__":
  pwdstr = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRTSUVXYZ1234567890`~!@#$%^&*()_-+={}[]\|:;'<>,.?/" + '"'
  str.join('', np.random.choice(list(pwdstr), 15))
