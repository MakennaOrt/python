class Television:
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self) -> None:
    '''
    This code is setting the instance variables status, muted, volume, and channel
    '''
    self.__status: bool = False
    self.__muted: bool = False
    self.__volume: int = self.MIN_VOLUME
    self.__channel: int = self.MIN_CHANNEL
  def power(self) -> None:
    '''
    This code is checking the power of the tv and adjusting accordingly
    :return: TV status
    '''
    if self.__status:
      self.__status = False
    else:
      self.__status = True
      
  def mute(self) -> None:
    '''
    This code is checking the muted status of the TV and adjusting accordingly
    :return: Mute Status
    '''
    if self.__status:
      if self.__muted:
        self.__muted = False
      else:
        self.__muted = True
        
  def channel_up(self) -> None:
    '''
    This code changes the channels up accordingly
    :return: New Channel
    '''
    if self.__status:
      self.__channel = min(self.__channel + 1, self.MIN_CHANNEL)
      
  def channel_down(self) -> None:
    '''
    This code changes the channels down accordingly
    :return: New Channel
    '''
    if self.__status:
      self.__channel = max(self.__channel - 1, self.MIN_CHANNEL)
      
  def volume_up(self) -> None:
    '''
    This code changes the volume up accordingly
    :return: new volume number
    '''
    if self.__volume < self.MAX_VOLUME and self.__status:
      self.__volume += 1
      
  def volume_down(self) -> None:
    '''
    This code changes the volume down accordingly 
    :return: new volume number 
    '''
    if self.__volume > self.MIN_VOLUME and self.__status:
      self.__volume -= 1
      
  def __str__(self) -> Str:
    '''
    This code prints the power status, channel number, and volume number accordingly
    :return: Power, Channel, and Volume print statment 
    '''
      return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
    
      
