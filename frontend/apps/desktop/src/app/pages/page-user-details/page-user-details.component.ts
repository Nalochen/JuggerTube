import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Router } from '@angular/router';

import {
  UiButtonColorEnum,
  UiButtonComponent,
} from '../../ui-button/ui-button.component';
import {
  UiInputComponent,
  UiInputTypeEnum,
} from '../../ui-input/ui-input.component';

export const userForm = new FormGroup<{
  email: FormControl<string>;
  password: FormControl<string>;
}>({
  email: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required, Validators.email],
  }),
  password: new FormControl(
    {
      value: '',
      disabled: true,
    },
    {
      nonNullable: true,
      validators: [Validators.required, Validators.minLength(8)],
    }
  ),
});

@Component({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    UiButtonComponent,
    UiInputComponent,
  ],
  standalone: true,
  templateUrl: './page-user-details.component.html',
  styleUrl: './page-user-details.component.less',
})
export class PageUserDetailsComponent {
  public user = {
    email: 'user.juli@gmx.de',
    username: 'nalochen',
    name: 'Nalo Uger',
    profilePicture: 'lundy_sheep.jpeg',
  };

  constructor(private router: Router) {}

  protected readonly form = userForm;

  public onSubmit(): void {
    if (!this.form.valid) {
      this.markAllFieldsAsTouched();
      return;
    }

    //this.authService.update(this.form.value);

    this.form.reset();

    this.router.navigate(['/user-details']);
  }

  public onDelete(): void {
    //this.authService.delete();
    //this.authService.logout(); falls noch nicht in delete passiert

    this.router.navigate(['/']);
  }

  private markAllFieldsAsTouched(): void {
    Object.keys(this.form.controls).forEach((field) => {
      const control = this.form.get(field);
      if (control instanceof FormControl) {
        control.markAsTouched({ onlySelf: true });
      }
    });
  }

  protected readonly UiButtonColorEnum = UiButtonColorEnum;
  protected readonly UiInputTypeEnum = UiInputTypeEnum;
}
