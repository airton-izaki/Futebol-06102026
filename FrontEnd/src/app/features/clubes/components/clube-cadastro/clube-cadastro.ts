import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { finalize, timeout } from 'rxjs';
import { ClubeCreate, GestaoEnum } from '../../models/clube.model';
import { Clube as ClubeService, EstadoResponse, CidadeResponse } from '../../services/clube';

// Módulos do PrimeNG
import { InputTextModule } from 'primeng/inputtext';
import { SelectModule } from 'primeng/select';
import { DatePickerModule } from 'primeng/datepicker';
import { ColorPickerModule } from 'primeng/colorpicker';
import { TextareaModule } from 'primeng/textarea';
import { CheckboxModule } from 'primeng/checkbox';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { DialogModule } from 'primeng/dialog';



@Component({
	selector: 'app-clube-cadastro',
	imports: [
    CommonModule,
    ReactiveFormsModule,
    InputTextModule,
    SelectModule,
    DatePickerModule,
    ColorPickerModule,
    TextareaModule,
    CheckboxModule,
    ButtonModule,
    CardModule,
    DialogModule
  ],
	templateUrl: './clube-cadastro.html',
	styleUrl: './clube-cadastro.css',
})
export class ClubeCadastro implements OnInit{
    clubeForm!: FormGroup;
    estados: EstadoResponse[] = [];
    cidades: CidadeResponse[] = [];
    carregandoEstados = false;
    carregandoCidades = false;
    erroLocalizacao = '';
    salvando = false;
    erroCadastro = '';
    modalSucessoVisivel = false;
    clubeCadastrado = '';
    idClubeCadastrado: number | null = null;

    gestaoOpcoes = [
      { label: 'Associativo', value: GestaoEnum.ASSOCIATIVO },
      { label: 'SAF', value: GestaoEnum.SAF },
      { label: 'Privado', value: GestaoEnum.PRIVADO },
      { label: 'Híbrido', value: GestaoEnum.HIBRIDO }
    ];

    constructor(private fb: FormBuilder, private clubeService: ClubeService) {}

    ngOnInit(): void {
      this.iniciarFormulario();
      this.carregarEstados();
      this.clubeForm.get('estado')?.valueChanges.subscribe((sigla: string) => {
        this.clubeForm.get('cidade')?.reset('');
        this.cidades = [];
        if (sigla) this.carregarCidades(sigla);
      });
    }

    private carregarEstados(): void {
      this.carregandoEstados = true;
      this.erroLocalizacao = '';
      this.clubeService.getEstados().subscribe({
        next: estados => { this.estados = estados; this.carregandoEstados = false; },
        error: erro => {
          console.error('Erro ao carregar estados:', erro);
          this.erroLocalizacao = erro.error?.detail
            ? `Erro ao carregar estados: ${erro.error.detail}`
            : `Não foi possível carregar os estados (HTTP ${erro.status || 'sem resposta'}). Verifique se a API está ativa.`;
          this.carregandoEstados = false;
        }
      });
    }

    private carregarCidades(sigla: string): void {
      this.carregandoCidades = true;
      this.erroLocalizacao = '';
      this.clubeService.getCidadesPorEstado(sigla).subscribe({
        next: cidades => { this.cidades = cidades; this.carregandoCidades = false; },
        error: erro => {
          console.error(`Erro ao carregar cidades de ${sigla}:`, erro);
          this.erroLocalizacao = erro.error?.detail
            ? `Erro ao carregar cidades: ${erro.error.detail}`
            : `Não foi possível carregar as cidades (HTTP ${erro.status || 'sem resposta'}).`;
          this.carregandoCidades = false;
        }
      });
    }

    private iniciarFormulario(): void {
    this.clubeForm = this.fb.group({
        nome_oficial: ['', [Validators.required, Validators.maxLength(100)]],
        nome: ['', [Validators.required, Validators.maxLength(100)]],
        sigla: ['', [Validators.required, Validators.maxLength(5)]],
        gestao: [GestaoEnum.ASSOCIATIVO, [Validators.required]],
        fundacao: [null, [Validators.required]],
        estado: ['', [Validators.required, Validators.minLength(2), Validators.maxLength(2)]],
        cidade: ['', [Validators.required, Validators.maxLength(100)]],
        estadio: ['', [Validators.maxLength(100)]],
        cor_primaria: ['#000000', [Validators.required, Validators.maxLength(30)]],
        cor_secundaria: ['#ffffff', [Validators.maxLength(30)]],
        cor_terciaria: ['', [Validators.maxLength(30)]],
        website: [''],
        escudo: [''],
        observacao: ['', [Validators.maxLength(500)]],
        ativo: [true]
      });
    }

    onSubmit(): void {
      this.erroCadastro = '';
      this.modalSucessoVisivel = false;

      if (this.clubeForm.invalid) {
        this.clubeForm.markAllAsTouched();
        return;
      }

      const valores = this.clubeForm.getRawValue();
      const dados: ClubeCreate = {
        ...valores,
        fundacao: this.formatarData(valores.fundacao)
      };

      this.salvando = true;
      this.clubeService.cadastrarClube(dados).pipe(
        timeout({ first: 20000 }),
        finalize(() => this.salvando = false)
      ).subscribe({
        next: clube => {
          this.clubeCadastrado = clube.nome;
          this.idClubeCadastrado = clube.id;
          this.modalSucessoVisivel = true;
        },
        error: erro => {
          const detalhe = erro.error?.detail;
          if (erro.name === 'TimeoutError') {
            this.erroCadastro = 'A API demorou para responder. Confira a lista de clubes antes de tentar novamente, para evitar um cadastro duplicado.';
          } else {
            this.erroCadastro = typeof detalhe === 'string'
              ? detalhe
              : `Não foi possível cadastrar o clube (HTTP ${erro.status || 'sem resposta'}). Verifique se a API está ativa.`;
          }
        }
      });
    }

    private formatarData(valor: Date | string): string {
      if (!(valor instanceof Date)) return String(valor).slice(0, 10);

      const ano = valor.getFullYear();
      const mes = String(valor.getMonth() + 1).padStart(2, '0');
      const dia = String(valor.getDate()).padStart(2, '0');
      return `${ano}-${mes}-${dia}`;
    }

}
