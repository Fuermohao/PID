<template>
  <div class="display-part">
    <mu-flex>
      <mu-flex class="tube1"
        align-items="end"
        align-content="end">
        <div id="flowin1"
          style="width:100%;height:70px"
          class="water"></div>
      </mu-flex>
      <div class="can-top">
        <mu-flex align-items="end"
          align-content="end">
          <mu-flex class="tube2"
            align-items="end"
            align-content="end">
            <div id="flowin2"
              style="width:100%;height:70px"
              class="water"></div>
          </mu-flex>

          <div id="flowin3"
            style="width:70px;height:75px"
            class="water"></div>

        </mu-flex>
      </div>

    </mu-flex>
    <mu-flex>
      <div class="spacer">

      </div>
      <div class="can">
        <div id="flowin4"
          class="flowin"></div>
        <div class="water"
          id="waterLev"
          style="height:100px;"></div>
      </div>
      <div>
        <div class="spacer-right">
          <mu-flex>
            <div class="target"></div>
            <p class="target-txt">Target</p>
          </mu-flex>

        </div>
        <mu-flex id="tube3"
          class="tube3"
          align-items="end"
          align-content="end">

          <div id="flowout"
            style="width:100%;height:40px"
            class="water">

          </div>
        </mu-flex>
      </div>
    </mu-flex>

  </div>
</template>

<script>
export default {
  mounted: function () {
    this.$nextTick(function () {

      setInterval(() => document.getElementById('calculator').click(), 50);
    })
  }
}
</script>

<style scoped>
.spacer {
  width: 150px;
  height: 80px;
}
.spacer-right {
  width: 100%;
  border-left: 5px solid #4e342e;
  height: 650px;
}

.target {
  width: 50px;
  height: 5px;
  position: relative;
  top: 400px;
  background: red;
}

.target-txt {
  position: relative;
  padding-left: 12px;
  top: 380px;
}

.tube1 {
  background: grey;
  /* background: #64b5f6; */
  width: 150px;
  height: 80px;
  border-top: 5px solid #4e342e;
  /* border-left: 5px solid #4e342e; */
  border-bottom: 5px solid #4e342e;
}

.tube2 {
  /* background: #64b5f6; */
  background: grey;
  width: 100px;
  height: 75px;
  border-bottom: 5px solid #4e342e;
}

.tube3 {
  /* background: #64b5f6; */
  background: grey;
  position: relative;
  /* top: 650px; */
  width: 100px;
  height: 50px;
  border-top: 5px solid #4e342e;
  /* border-right: 5px solid #4e342e; */
  border-bottom: 5px solid #4e342e;
}
.can {
  background: grey;
  width: 495px;
  height: 700px;
  border-left: 5px solid #4e342e;
  /* border-right: 5px solid #4e342e; */
  border-bottom: 5px solid #4e342e;
}

.can-top {
  background: grey;
  width: 500px;
  height: 80px;
  border-top: 5px solid #4e342e;
  /* border-right: 5px solid #4e342e; */
  /* border-bottom: 5px solid #4e342e; */
}

.flowin {
  width: 70px;
  left: 95px;
  background: #64b5f6;
  position: relative;
}

.pane-layout {
  width: 100vw;
  height: 100vh;
  padding: 0;
  margin: 0;
}
.water {
  width: 100%;
  background: #64b5f6;
  position: relative;
}
.display-part {
  width: 100%;
  height: 100%;
  /* background: grey; */
  padding: 64px;
  margin: 0;
}
</style>
