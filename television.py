class Television:
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self):
    self.__status = False
    self.__muted = False
    self.__volume = self.MIN_VOLUME
    self.__channel = self.MIN_CHANNEL
  def power(self):
    if self.__status:
      self.__status = False
    else:
      self.__status = True
  def mute(self):
    if self.__status:
      if self.__muted:
        self.__muted = False
      else:
        self.__muted = True
  def channel_up(self):
    if self.__status:
      self.__channel = min(self.__channel + 1, self.MIN_CHANNEL)
  def channel_down(self):
    if self.__status:
      self.__channel = max(self.__channel - 1, self.MIN_CHANNEL)
  def volume_up(self):
    if self.__volume < self.MAX_VOLUME and self.__status:
      self.__volume += 1
  def volume_down(self):
    if self.__volume > self.MIN_VOLUME and self.__status:
      self.__volume -= 1
  def __str__(self):
      return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
    
      
