import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Clube as ClubeDados } from '../../models/clube.model';
import { Clube as ClubeApi } from '../../services/clube';

@Component({
  selector: 'app-clube-lista',
  imports: [CommonModule, RouterLink],
  templateUrl: './clube-lista.html',
  styleUrl: './clube-lista.css',
})
export class ClubeLista implements OnInit {
  clubes: ClubeDados[] = [];
  carregando = true;
  erro = '';

  constructor(private clubeApi: ClubeApi) {}

  ngOnInit(): void {
    this.carregarClubes();
  }

  carregarClubes(): void {
    this.carregando = true;
    this.erro = '';

    this.clubeApi.listarClubes().subscribe({
      next: clubes => {
        this.clubes = clubes;
        this.carregando = false;
      },
      error: resposta => {
        this.erro = resposta.error?.detail
          ?? `Não foi possível carregar os clubes (HTTP ${resposta.status || 'sem resposta'}). Verifique se a API está ativa.`;
        this.carregando = false;
      }
    });
  }
}
