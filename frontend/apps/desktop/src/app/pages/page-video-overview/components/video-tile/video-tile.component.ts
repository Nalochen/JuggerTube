import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

import { Video } from '../../../../app.component';

@Component({
  selector: 'video-tile',
  imports: [CommonModule],
  standalone: true,
  templateUrl: './video-tile.component.html',
  styleUrl: './video-tile.component.less',
})
export class VideoTileComponent {
  @Input() public video!: Video;
}
