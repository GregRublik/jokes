from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = interface.QueryInterface(IAudioEndpointVolume)
current_volume = volume.GetMasterVolumeLevel()  # Получить текущий уровень


def volume_remove(num: float | int | None = None):
    if num:
        volume.SetMasterVolumeLevelScalar(num, None)
        return volume.GetMasterVolumeLevelScalar()
    return volume.GetMasterVolumeLevelScalar()
