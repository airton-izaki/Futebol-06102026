import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Clube as ClubeResponse, ClubeCreate } from '../models/clube.model';


export interface EstadoResponse {
  id: number;
  sigla: string;
  nome: string;
}

export interface CidadeResponse {
  id: number;
  nome: string;
}


@Injectable({
  providedIn: 'root',
})
export class Clube {

  private readonly apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getEstados(): Observable<EstadoResponse[]> {
    return this.http.get<EstadoResponse[]>(`${this.apiUrl}/ibge/estados`);
  }

  getCidadesPorEstado(siglaUf: string): Observable<CidadeResponse[]> {
    return this.http.get<CidadeResponse[]>(`${this.apiUrl}/ibge/estados/${siglaUf}/cidades`);
  }

  listarClubes(): Observable<ClubeResponse[]> {
    return this.http.get<ClubeResponse[]>(`${this.apiUrl}/clubes/`);
  }

  buscarClube(id: number): Observable<ClubeResponse> {
    return this.http.get<ClubeResponse>(`${this.apiUrl}/clubes/${id}`);
  }

  cadastrarClube(dados: ClubeCreate): Observable<ClubeResponse> {
    return this.http.post<ClubeResponse>(`${this.apiUrl}/clubes/`, dados);
  }

  atualizarClube(id: number, dados: ClubeCreate): Observable<ClubeResponse> {
    return this.http.put<ClubeResponse>(`${this.apiUrl}/clubes/${id}`, dados);
  }

}
