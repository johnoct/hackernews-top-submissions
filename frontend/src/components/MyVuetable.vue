// MyVuetable.vue

<template>
  <vuetable ref="vuetable"
    api-url="https://young-retreat-74774.herokuapp.com/top_hn_subs"
    :fields="fields"
  >
  </vuetable>
</template>

<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'

export default {
  components: {
    Vuetable
  },
  data () {
    return {
      fields: [
        'score',
        'title',
        {
          name: 'link',   
          callback: 'makeUrl'
        }
      ]
    }
  },
  methods: {
    makeUrl (value) {
      return '<a href="' +value+'">'+value +' </a>';
    }
  }
}
</script>