#include <stdbool.h>
#include <stdio.h>

void tabela_price_sac(){
	int i, opcao; 
	float parcela,capital, taxa, tempo, a, b, c, d, amortizacao;
	bool sla = true;
	
	printf("me informe o valor da capital: ");
	scanf("%f", &capital);
	
	printf("me informe a taxa(em porcentagem): ");
	scanf("%f", &taxa);
	
	taxa = taxa / 100;
	
	printf("me informe o tempo(em meses): ");
	scanf("%f", &tempo);
	
	while(sla){
		printf("me informe qual tipo de tabela voce quer? sac(1) price(2): ");
		scanf("%d", &opcao);
	
		if(opcao == 1){

			
			amortizacao = capital / tempo;
			
			for(i = 1; i <= tempo; i++){
				
				a = capital * taxa;
				parcela = a + amortizacao;
				capital = capital - amortizacao;
				
				printf("\n\nmes %d", i);
				printf("\namortizacao: %.2f", amortizacao);
				printf("\njuros: %.2f", a);
				printf("\nparcela: %.2f", parcela);
				printf("\nvalor devedor: %.2f", capital);
			}
			printf("\n\ndeseja continuar? sim(1) / nao(2)");
			scanf("%d", &opcao);
			if(opcao == 2){
				break;
			}
		}else if(opcao == 2){

			a = capital * taxa;
			b = taxa + 1;
			c = b * b;
			
			for(i = 2; i < tempo; i++){
				c = c * b;
			}
			
			b = a * c;
			a = c - 1;
			
			parcela = b / a;
			
			
			for(i = 1; i <= tempo; i++){
				a = capital * taxa;
				amortizacao = parcela - a;
				capital = capital - amortizacao;
				
				printf("\n\nMes %d", i);
				printf("\nparcela: %.2f", parcela);
				printf("\njuros: %.2f", a);
				printf("\namortizacao: %.2f", amortizacao);
				printf("\nsaldo devedor: %.2f", capital);
			}
			printf("\n\ndeseja continuar? sim(1) / nao(2)");
			scanf("%d", &opcao);
			if(opcao == 2){
				break;
			}
		} else{
			printf("informe um valor valido\n\n");
		
		}
	}
}

int main(){
	tabela_price_sac();
}