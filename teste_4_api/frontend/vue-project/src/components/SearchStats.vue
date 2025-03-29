<template>
    <div class="search-stats">
      <p>Encontrados {{ count }} resultados para "{{ query }}"</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ['query', 'count']
  };
  </script>
  