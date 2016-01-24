'''    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import xbmc
import dbus
import xbmcaddon
from  time import time as now

class Service(xbmc.Player):
  def __init__(self):
    xbmc.Player.__init__(self)
    self.paused_at = 0
    self.addon = xbmcaddon.Addon('service.pausespotify')
    self.bus = dbus.SessionBus(private=True)
    self.spotify = self.bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    self.spotify = dbus.Interface(self.spotify, 'org.mpris.MediaPlayer2.Player')
    xbmc.log('pausespotify - started')

  def onPlayBackStarted(self):
    xbmc.log('pausespotify - pause')
    self.spotify.Pause()
    self.paused_at = now()

  def onPlayBackStopped(self):
    self.onPlayBackFinished()

  def onPlayBackEnded(self):
    self.onPlayBackFinished()

  def onPlayBackFinished(self):
    wait_time = int(self.addon.getSetting('play_after_pause_time'))
    diff = now() - self.paused_at
    if diff <= wait_time:
      self.spotify.Play()
