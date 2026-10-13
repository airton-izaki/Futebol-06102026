// 1. Enum correspondente
export enum GestaoEnum {
  ASSOCIATIVO = "Associativo",
  SAF = "SAF",
  PRIVADO = "Privado",
  HIBRIDO = "Híbrido"
}

// 2. Interface para os dados do clube (Response)
export interface Clube {
  id: number;
  nome_oficial: string;
  nome: string;
  sigla: string;
  gestao: GestaoEnum;
  fundacao: string; // No Angular/JSON datas costumam vir como string (YYYY-MM-DD)
  estado: string;
  cidade: string;
  estadio?: string;
  cor_primaria: string;
  cor_secundaria?: string;
  cor_terciaria?: string;
  website?: string;
  escudo?: string;
  observacao?: string;
  ativo: boolean;
  criado_em: string;
  atualizado_em: string;
}

// 3. Interface para criação (sem id e datas automáticas)
export type ClubeCreate = Omit<Clube, 'id' | 'criado_em' | 'atualizado_em'>;
