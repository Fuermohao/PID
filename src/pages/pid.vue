<template>
  <split-pane ref="splitVertical"
    :min-percent="0"
    :default-percent="50"
    split="vertical"
    class="pane-layout">
    <template slot="paneL"
      class="left-pane">
      <can />
    </template>

    <template slot="paneR">

      <editor ref="editor"
        class="editor"></editor>

    </template>
  </split-pane>
</template>

<script>
import SplitPane from "@/components/SplitPane";
import Editor from "@/components/Editor";
import Can from "@/components/Can";

export default {
  components: {
    SplitPane,
    Editor,
    Can
  },
  mounted: function() {
    this.$nextTick(function() {
      // window.onresize = () => {
      //   return () => that.$refs.editor.layout();
      // }
    });
  },
  methods: {
    
  }
};
</script>

<style scoped>
.pane-layout {
  width: 100vw;
  height: 100vh;
  padding: 0;
  margin: 0;
}

.editor {
  width: 100%;
  height: 100%;
}
</style>
