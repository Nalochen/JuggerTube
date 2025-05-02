import { CommonModule } from '@angular/common';
import { Component, Signal, computed, signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { SearchVideoTileComponent } from './components/search-video-tile/search-video-tile.component';
import { VideoTileComponent } from './components/video-tile/video-tile.component';
import { VideosDataService } from '@frontend/video';
import { VideoApiResponseModel } from '@frontend/video-data';
import {MatPaginatorModule} from '@angular/material/paginator';

@Component({
  imports: [
    CommonModule,
    VideoTileComponent,
    SearchVideoTileComponent,
    RouterLink,
    MatPaginatorModule
  ],
  standalone: true,
  templateUrl: './page-video-overview.component.html',
  styleUrl: './page-video-overview.component.less',
})
export class PageVideoOverviewComponent {
  public readonly videos: Signal<VideoApiResponseModel[]>;
  public readonly paginatedVideos: Signal<VideoApiResponseModel[]>;
  public readonly pageSizeOptions = [5, 10, 25, 50];
  public readonly showFirstLastButtons = true;
  private readonly _pageSize = signal(10);
  private readonly _pageIndex = signal(0);

  public get pageSize(): number {
    return this._pageSize();
  }

  public get pageIndex(): number {
    return this._pageIndex();
  }

  constructor(private readonly videosDataService: VideosDataService) {
    this.videosDataService.loadVideos();
    this.videos = this.videosDataService.videos;
    this.paginatedVideos = computed(() => {
      const start = this._pageIndex() * this._pageSize();
      const end = (this._pageIndex() + 1) * this._pageSize();
      return this.videos().slice(start, end);
    });
  }

  public handlePageEvent(event: any): void {
    this._pageSize.set(event.pageSize);
    this._pageIndex.set(event.pageIndex);
  }
}
