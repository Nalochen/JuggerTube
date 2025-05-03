import { CommonModule } from '@angular/common';
import {Component, Signal} from '@angular/core';
import { RouterLink } from '@angular/router';

import {MatPaginatorModule, PageEvent} from '@angular/material/paginator';

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
  public limit = 20;
  public start = 1;
  private loadedRanges: Set<number> = new Set();

  constructor(private readonly videosDataService: VideosDataService) {
    this.videosDataService.loadPaginatedVideos(this.start, this.limit);
    this.paginatedVideos = this.videosDataService.paginatedVideos;
    this.totalVideos = this.videosDataService.totalCountVideos;
    this.loadedRanges.add(this.limit);
  }

  private isRangeLoaded(startIndex: number): boolean {
    return this.loadedRanges.has(startIndex);
  }

  public handlePageEvent(event: PageEvent): void {
    const newStart = event.pageIndex + 1; // Convert from 0-based to 1-based indexing
    this.start = newStart;
    this.limit = event.pageSize;

    // Check if we need to load this range
    if (!this.isRangeLoaded(newStart)) {
      this.loadedRanges.add(newStart);
      this.videosDataService.loadNextVideos(newStart, this.limit);
    } else {
      // If range is already loaded, just update the view
      this.videosDataService.loadPaginatedVideos(newStart, this.limit);
    }
  }

  // Helper method to convert 1-based index to 0-based for the paginator
  public get currentPageIndex(): number {
    return this.start - 1;
  }
}
