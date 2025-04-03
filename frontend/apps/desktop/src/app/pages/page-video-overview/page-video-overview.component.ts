import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

import { TagContent, Video } from '../../app.component';

import { SearchVideoTileComponent } from './components/search-video-tile/search-video-tile.component';
import { VideoTileComponent } from './components/video-tile/video-tile.component';

@Component({
  imports: [CommonModule, VideoTileComponent, SearchVideoTileComponent],
  standalone: true,
  templateUrl: './page-video-overview.component.html',
  styleUrl: './page-video-overview.component.less',
})
export class PageVideoOverviewComponent {
  public videos: Video[] = [
    {
      id: 1,
      title: 'Title Video 1',
      description: 'Video 1 description',
      url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
      uploadedAt: '2025-01-01 10:00',
      createdAt: '2025-01-01 10:00',
      tags: [TagContent.TRAINING],
      channel: {
        id: 1,
        name: 'Channel 1',
        escapedName: 'channel-1',
      },
    },
    {
      id: 2,
      title: 'Title Video 2',
      description: 'Video 1 description',
      url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
      uploadedAt: '2025-01-01 10:00',
      createdAt: '2025-01-01 10:00',
      tags: [TagContent.TRAINING],
      channel: {
        id: 1,
        name: 'Channel 1',
        escapedName: 'channel-1',
      },
    },
    {
      id: 3,
      title: 'Title Video 3',
      description: 'Video 1 description',
      url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
      uploadedAt: '2025-01-01 10:00',
      createdAt: '2025-01-01 10:00',
      tags: [TagContent.PODCAST],
      channel: {
        id: 1,
        name: 'Channel 1',
        escapedName: 'channel-1',
      },
    },
    {
      id: 4,
      title: 'Title Video 4',
      description: 'Video 1 description',
      url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
      uploadedAt: '2025-01-01 10:00',
      createdAt: '2025-01-01 10:00',
      tags: [TagContent.HIGHLIGHTS, TagContent.TRAINING],
      channel: {
        id: 1,
        name: 'Channel 1',
        escapedName: 'channel-1',
      },
    },
  ];
}
