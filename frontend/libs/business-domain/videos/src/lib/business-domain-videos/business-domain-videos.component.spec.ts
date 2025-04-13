import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BusinessDomainVideosComponent } from '@frontend/business-domain-videos';

describe('BusinessDomainVideosComponent', () => {
  let component: BusinessDomainVideosComponent;
  let fixture: ComponentFixture<BusinessDomainVideosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BusinessDomainVideosComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(BusinessDomainVideosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
