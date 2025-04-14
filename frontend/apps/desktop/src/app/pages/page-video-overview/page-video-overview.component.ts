import { CommonModule } from '@angular/common';
import { Component, Signal } from '@angular/core';

import { SearchVideoTileComponent } from './components/search-video-tile/search-video-tile.component';
import { VideoTileComponent } from './components/video-tile/video-tile.component';
import { VideosDataService } from '@frontend/business-domain-videos';
import { VideoApiResponseModel } from '@frontend/data-domain-videos';

@Component({
  imports: [CommonModule, VideoTileComponent, SearchVideoTileComponent],
  standalone: true,
  templateUrl: './page-video-overview.component.html',
  styleUrl: './page-video-overview.component.less',
})
export class PageVideoOverviewComponent {
  public readonly videos: Signal<VideoApiResponseModel[]>;

  constructor(private readonly videosDataService: VideosDataService) {
    this.videosDataService.loadVideos();
    this.videos = this.videosDataService.videos;
  }
}
