# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor
from ..utils import (
    urlencode_postdata,
    parse_filesize,
    clean_html,
)

class VeraIE(InfoExtractor):
    _VALID_URL = r'''(?x)
                    https?://
                        (?P<host>
                            (?:www\.)?
                            (?:
                                tv\.vera\.(?:com\.uy|uy)|
                                veramas\.(?:com\.uy|uy)
                            )
                        )/
                        (?:f|video|veramas\/vod)/
                        (?P<id>[a-zA-Z0-9-_]+)
                  '''

    _TEST = {
        'url': 'https://tv.vera.com.uy/video/38478',
        'info_dict': {
            'id': '38478',
            'ext': 'mp4',
            'title': 'Trailer 4',
            'thumbnail': r're:^https?://.*\.jpg$',
        }
    }

    def _real_extract(self, url):

        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')
        webpage = self._download_webpage(url, 'ID: ' + video_id)
        base_content = clean_html(webpage)

        title = self._html_search_regex(
            r'<h2 class="left">([^<]+)</h2>', webpage, 'title')

        description = self._html_search_regex(
            r'(?s)<div\b[^>]+\bclass=["\']info-canal[^>]+>(.+?)</div>',
            webpage, 'description', fatal=False)

        ext = self._html_search_meta(
            'encodingFormat', webpage, 'ext', default='.mp4')[1:]

        search_iframe = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', base_content)
        key_search_iframe = ['syndication']
        iframeLink = [s for s in search_iframe if any(xs in s for xs in key_search_iframe)]
        iframe = ''.join( c for c in iframeLink if  c not in "');" )
        #print("LINK 1 →", iframe)

        iframe_content = self._download_webpage(iframe, 'Media')

        search_media = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', iframe_content)
        key_search_media = ['.m3u8']
        mediaLink = [s for s in search_media if any(xs in s for xs in key_search_media)]
        video_url = ''.join( c for c in mediaLink if  c not in "');" )
        #print("LINK 2 →", video_url)

        # CHECK DATA ↓
        verDatos = url, title, description, ext, video_id, mobj
        #print(verDatos)

        return {
            'url': video_url,
            'id': video_id,
            'title': title,
            'description': description,
            'ext': ext,
        }
