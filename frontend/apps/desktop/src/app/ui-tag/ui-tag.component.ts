import { CommonModule } from '@angular/common';
import { Component, HostBinding, Input } from '@angular/core';

@Component({
  selector: 'ui-tag',
  imports: [CommonModule],
  templateUrl: './ui-tag.component.html',
  styleUrl: './ui-tag.component.less',
})
export class UiTagComponent {
  @Input() public category!: string;

  @HostBinding('class')
  private get hostClass(): string {
    return this.category;
  }
}
