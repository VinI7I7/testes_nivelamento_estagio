<template>
    <section class="search-container">
      <div class="search-box">
        <input 
          type="text" 
          v-model="query" 
          @input="onInput"
          placeholder="Digite para buscar operadoras..." 
          class="search-input"
        />
        <button @click="onSearch" class="search-button">Buscar</button>
      </div>
    </section>
  </template>
  
  <script>
  import { debounce } from 'lodash';
  
  export default {
    props: ['modelValue'],
    emits: ['update:modelValue', 'search'],
    data() {
      return { query: this.modelValue };
    },
    watch: {
      modelValue(newVal) {
        this.query = newVal;
      }
    },
    created() {
      this.debouncedSearch = debounce(() => this.$emit('search'), 500);
    },
    methods: {
      onInput() {
        this.$emit('update:modelValue', this.query);
        if (this.query.length >= 3) this.debouncedSearch();
      },
      onSearch() {
        this.$emit('search');
      }
    }
  };
  </script>
  