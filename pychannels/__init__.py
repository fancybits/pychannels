# -*- coding: utf-8 -*-

"""
PyChannels
~~~~~~~~~~
*PyChannels* is a client, written in Python, for talking to an instance of
the Channels app on your network. Channels runs on streaming boxes like the
Apple TV and NVIDIA SHIELD. This is a simple client. Learn more in the README.
https://getchannels.com/api
https://getchannels.com
:copyright: (c) 2020 by Fancy Bits, LLC.
:license: MIT, see LICENSE for more details
"""

import requests
import json

TIMEOUT = 1

class Channels(object):
    def __init__(self, host, port=57000):
        """Initialize the Channels client."""
        self.host = host
        self.port = port

    @property
    def _base_url(self):
        """Return the base url for endpoints."""
        return "http://" + self.host + ":" + str(self.port)

    def _request(self, method, path, params=None):
        """Make the actual request and returns the parsed response."""
        url = self._base_url + path
        headers = {'Content-Type': 'application/json'}

        try:
            if method == 'GET':
                response = requests.get(url, timeout=TIMEOUT, headers=headers)
            elif method == "POST":
                response = requests.post(url, json=params, timeout=TIMEOUT, headers=headers)
            elif method == "PUT":
                response = requests.put(url, json=params, timeout=TIMEOUT, headers=headers)
            elif method == "DELETE":
                response = requests.delete(url, timeout=TIMEOUT, headers=headers)

            if response:
                return response.json()
            else:
                return {'status': 'error'}
        except requests.exceptions.HTTPError:
            return {'status': 'error'}
        except requests.exceptions.Timeout:
            return {'status': 'offline'}
        except requests.exceptions.RequestException:
            return {'status': 'offline'}

    def _command(self, named_command):
        """Make a request for a controlling command."""
        return self._request('POST', '/api/' + named_command)

    def status(self):
        """Return the current state."""
        return self._request('GET', '/api/status')

    def favorite_channels(self):
        """Return the favorite channels."""
        response = self._request('GET', '/api/favorite_channels')
        if type(response) is list:
            return response
        else:
        	return []

    def toggle_mute(self):
        """Toggle mute state and returns the current state."""
        return self._command('toggle_mute')

    def toggle_cc(self):
        """Toggle captions state and returns the current state."""
        return self._command('toggle_cc')

    def toggle_record(self):
        """Record the program playing on the current channel."""
        return self._command('toggle_record')

    def channel_up(self):
        """Change the channel and returns the current state."""
        return self._command('channel_up')

    def channel_down(self):
        """Change the channel and returns the current state."""
        return self._command('channel_down')

    def previous_channel(self):
        """Jump back to the last channel."""
        return self._command('previous_channel')

    def toggle_pause(self):
        """Toggle paused state and returns the current state."""
        return self._command('toggle_pause')

    def pause(self):
        """Set playback to paused and returns the current state."""
        return self._command('pause')

    def resume(self):
        """Set playback to play and returns the current state."""
        return self._command('resume')

    def stop(self):
        """Set playback to stop and returns the current state."""
        return self._command('stop')

    def seek(self, seconds):
        """Seek number of seconds."""
        seconds = str(seconds or 0)
        return self._command('seek/' + seconds)

    def seek_forward(self):
        """Seek forward."""
        return self._command('seek_forward')

    def seek_backward(self):
        """Seek backward."""
        return self._command('seek_backward')

    def skip_forward(self):
        """Skip forward to the next chapter mark."""
        return self._command('skip_forward')

    def skip_backward(self):
        """Skip backward to the previous chapter mark."""
        return self._command('skip_backward')

    def toggle_muted(self):
        """Mute and returns the current state."""
        return self._command('toggle_mute')

    def play_channel(self, channel_number):
        """Set a channel to play and returns the current state."""
        return self._command('play/channel/' + str(channel_number))

    def play_recording(self, recording_id):
        """Set a recording to play and returns the current state."""
        return self._command('play/recording/' + str(recording_id))

    def navigate(self, section):
        """Change to a section of the app by providing its name and returns success status"""
        return self._command('navigate/' + section)

    def notify(self, title, message):
        """Present a notification while playing video and returns success status."""
        return self._request('POST', '/api/notify', {'title': title, 'message': message})
