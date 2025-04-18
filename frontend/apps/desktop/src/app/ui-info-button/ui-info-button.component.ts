import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

import { MatButtonModule } from '@angular/material/button';

import {
  UiButtonColorEnum,
  UiButtonComponent,
  UiButtonTypeEnum,
} from '../ui-button/ui-button.component';
import { Popover } from 'primeng/popover';

@Component({
  selector: 'ui-info-button',
  imports: [CommonModule, MatButtonModule, UiButtonComponent, Popover],
  standalone: true,
  templateUrl: './ui-info-button.component.html',
  styleUrls: ['./ui-info-button.component.less'],
})
export class UiInfoButtonComponent {
  protected readonly UiButtonTypeEnum = UiButtonTypeEnum;
  protected readonly UiButtonColorEnum = UiButtonColorEnum;
}
