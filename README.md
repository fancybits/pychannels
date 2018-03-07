<p align="center">
<a href="https://getchannels.com"><img src="http://getchannels.com/assets/img/icon-1024.png" width="256"></a>
</p>

# PyChannels!!

This is a simple client that lets you talk to the [Channels](https://getchannels.com) app while it's running.

## How to use it

Just create a new client and give it the host name of the device that Channels is running on. You can optionally pass in a port, which defaults to `57000`.

```python
from pychannels import Channels

client = Channels("192.168.1.192", 57000)

client.pause()
client.resume()
client.stop()
```

## API

All responses return the current status of Channels. You can get this simply with `client.status()`, but every other method will return it as well.

### Status Data

Status data is returned as a simple Dict. Here's an example.

```python
{
  'status': 'paused',
  'muted': False,
  'channel': {
    'number': '35.1',
    'name': 'Fox-HD',
    'image_url': 'http://fanc.tmsimg.com/h5/NowShowing/28719/s28719_h5_aa.png'
  },
  'now_playing': {
    'title': 'The Mick',
    'season_number': 2,
    'episode_number': 16,
    'episode_title': 'The Accident',
    'image_url': 'http://fanc.tmsimg.com/assets/p12900954_b_h6_ad.jpg',
    'summary': 'Chip offers to help Sabrina get a fake ID in exchange for a night out with her and her friends.'
  }
}
```

### Info

You can fetch 2 sets of information from Channels. Its current status and the
current set of favorite channels.

#### Status

    client.status()

This returns the result documented above.


#### Favorite Channels

    client.favorite_channels()

This returns an array of channel Dicts. Here's an example.

```python
[{
	'number': '12.1',
	'call_sign': 'WWBT-HD',
	'image_url': 'http://fanc.tmsimg.com/h5/NowShowing/28717/s28717_h5_aa.png',
	'name': 'NBC HD',
	'hd': True
}, {
	'number': '35.1',
	'call_sign': 'Fox-HD',
	'image_url': 'http://fanc.tmsimg.com/h5/NowShowing/28719/s28719_h5_aa.png',
	'name': 'Fox-HD',
	'hd': True
}, {
	'number': '552',
	'call_sign': 'TBS HD',
	'image_url': 'http://fanc.tmsimg.com/h5/NowShowing/58515/s58515_h5_aa.png',
	'name': 'TBS HD',
	'hd': True
}, {
	'number': '570',
	'call_sign': 'ESPN HD',
	'image_url': 'http://fanc.tmsimg.com/h5/NowShowing/32645/s32645_h5_aa.png',
	'name': 'ESPN HD',
	'hd': True
}]
```

### Commands

You can control Channels with these methods.

#### Toggle Mute
    client.toggle_mute()

#### Pause
    client.pause()

#### Resume
    client.resume()

#### Stop
    client.stop()

#### Seek By
    client.seek_by(seconds)
Seek forward or backward on the timeline with an inputted number of seconds. Negative values go backward.

#### Seek Forward
    client.seek_forward()
Seek forward in the timeline by the set number of seconds in Channels.

#### Seek Backward
    client.seek_backward()
Seek backward in the timeline by the set number of seconds in Channels.

#### Skip Forward
    client.skip_forward()
Skip to the next chapter mark. This is for recordings made with Channels DVR that have their commercials indexed.

#### Skip Backward
    client.skip_backward()
Skip to the previous chapter mark. This is for recordings made with Channels DVR that have their commercials indexed.

#### Play Channel
    client.play_channel(channel_number)
Play a channel by passing it the channel number.

#### Play Recording
    client.play_recording(recording_id)
Play a recording from Channels DVR

## Contributions

* fork
* create a feature branch
* open a Pull Request
