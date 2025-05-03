import { CommonModule } from '@angular/common';
import { Component, Signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { MatPaginatorModule, PageEvent } from '@angular/material/paginator';

import { SearchVideoTileComponent } from './components/search-video-tile/search-video-tile.component';
import { VideoTileComponent } from './components/video-tile/video-tile.component';
import { VideosDataService } from '@frontend/video';
import { VideoApiResponseModel } from '@frontend/video-data';

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
  public readonly paginatedVideos: Signal<VideoApiResponseModel[]>;
  public readonly totalVideos: Signal<number>;
  public readonly pageSizeOptions = [5, 10, 25, 50];
  public pageSize = 20;
  public startIndex = 0;
  public pageIndex = 0;

  constructor(private readonly videosDataService: VideosDataService) {
    this.videosDataService.loadPaginatedVideos(this.startIndex, this.pageSize);
    this.paginatedVideos = this.videosDataService.paginatedVideos;
    this.totalVideos = this.videosDataService.totalCountVideos;
  }

  public handlePageEvent(event: PageEvent): void {
    const newPageSize = event.pageSize;
    let targetPageIndex = event.pageIndex;

    if (newPageSize !== this.pageSize) {
      targetPageIndex = Math.floor(this.startIndex / newPageSize);
    }

    const targetStartIndex = targetPageIndex * newPageSize;
    const maxStartIndex = Math.max(0, Math.ceil(this.totalVideos() / newPageSize) - 1) * newPageSize;

    if (targetStartIndex >= this.totalVideos()) {
      this.navigateToPage(maxStartIndex, newPageSize);
      return;
    }

    this.navigateToPage(targetStartIndex, newPageSize);
  }

  private navigateToPage(startIndex: number, pageSize: number): void {
    this.pageIndex = startIndex / pageSize;
    this.startIndex = startIndex;
    this.pageSize = pageSize;

    if (!this.videosDataService.isRangeCached(startIndex, pageSize)) {
      this.videosDataService.loadNextVideos(startIndex, pageSize);
    } else {
      this.videosDataService.updateCurrentView(startIndex, pageSize);
    }
  }
}
