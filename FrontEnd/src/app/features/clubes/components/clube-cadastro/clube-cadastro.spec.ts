import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClubeCadastro } from './clube-cadastro';

describe('ClubeCadastro', () => {
  let component: ClubeCadastro;
  let fixture: ComponentFixture<ClubeCadastro>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ClubeCadastro],
    }).compileComponents();

    fixture = TestBed.createComponent(ClubeCadastro);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
