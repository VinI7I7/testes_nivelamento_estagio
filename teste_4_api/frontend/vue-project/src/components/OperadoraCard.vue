<template>
    <div class="operadora-card" @click="toggle">
      <div class="card-header">
        <h3>{{ operadora.Razao_Social || 'Nome não disponível' }}</h3>
        <span class="modalidade">{{ operadora.Modalidade || 'N/A' }}</span>
      </div>
  
      <div class="card-body">
        <p v-if="operadora.Nome_Fantasia"><strong>Nome Fantasia:</strong> {{ operadora.Nome_Fantasia }}</p>
        <p v-if="operadora.Registro_ANS"><strong>Registro ANS:</strong> {{ operadora.Registro_ANS }}</p>
        <p v-if="operadora.CNPJ"><strong>CNPJ:</strong> {{ operadora.CNPJ }}</p>
  
        <div v-if="expanded" class="card-details">
          <hr>
          <h4>Informações detalhadas</h4>
          <p v-if="operadora.Logradouro"><strong>Endereço:</strong> {{ operadora.Logradouro }}, {{ operadora.Numero }} {{ operadora.Complemento || '' }}</p>
          <p v-if="operadora.Bairro || operadora.Cidade || operadora.UF">
            {{ operadora.Bairro }}, {{ operadora.Cidade }}/{{ operadora.UF }} - CEP: {{ operadora.CEP }}
          </p>
          <p v-if="operadora.DDD || operadora.Telefone"><strong>Telefone:</strong> ({{ operadora.DDD }}) {{ operadora.Telefone }}</p>
          <p v-if="operadora.Endereco_eletronico"><strong>E-mail:</strong> {{ operadora.Endereco_eletronico }}</p>
          <p v-if="operadora.Representante"><strong>Representante:</strong> {{ operadora.Representante }} ({{ operadora.Cargo_Representante }})</p>
        </div>
  
        <button class="toggle-button" @click.stop="toggle">
          {{ expanded ? 'Menos detalhes' : 'Mais detalhes' }}
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['operadora', 'expanded'],
    emits: ['toggle'],
    methods: {
      toggle() {
        this.$emit('toggle');
      }
    }
  };
  </script>
  