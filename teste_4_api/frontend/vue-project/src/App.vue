<template>
  <div id="app">
    <header>
      <h1>Consulta de Operadoras</h1>
    </header>

    <SearchBox v-model="searchQuery" @search="performSearch" />
    <SearchStats v-if="hasSearched" :query="lastQuery" :count="results.length" />

    <section class="results-container">
      <Loading v-if="loading" />
      <NoResults v-else-if="results.length === 0 && hasSearched" :query="lastQuery" />
      
      <div v-else class="results-list">
        <OperadoraCard 
          v-for="(operadora, index) in results" 
          :key="index" 
          :operadora="operadora"
          :expanded="expandedIndex === index"
          @toggle="toggleDetails(index)"
        />
      </div>
    </section>
  </div>
</template>

<script>
import SearchBox from './components/SearchBox.vue';
import SearchStats from './components/SearchStats.vue';
import OperadoraCard from './components/OperadoraCard.vue';
import Loading from './components/Loading.vue';
import NoResults from './components/NoResults.vue';
import apiService from './components/apiService';


export default {
  name: 'App',
  components: { SearchBox, SearchStats, OperadoraCard, Loading, NoResults },
  data() {
    return {
      searchQuery: '',
      results: [],
      loading: false,
      lastQuery: '',
      hasSearched: false,
      expandedIndex: null,
    };
  },
  methods: {
    async performSearch() {
      if (this.searchQuery.length < 3) return;

      this.loading = true;
      this.lastQuery = this.searchQuery;
      this.hasSearched = true;

      try {
        this.results = await apiService.search(this.searchQuery);
      } catch (error) {
        console.error('Erro na busca:', error);
        this.results = [];
      } finally {
        this.loading = false;
      }
    },
    toggleDetails(index) {
      this.expandedIndex = this.expandedIndex === index ? null : index;
    }
  }
};
</script>

<style>
@import './assets/global.css';
</style>
