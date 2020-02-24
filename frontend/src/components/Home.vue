<template>
  <v-container>

    <v-row justify="center">
      <v-col cols="10" md="6">

        <v-slider
          color="blue"
          class="mt-12"
          v-model="sepalLength"
          label="Sepal Length (cm)"
          thumb-label="always"
          max="10"
          min="1"
          step="0.1"
        ></v-slider>

        <v-slider
          color="purple"
          class="mt-12"
          v-model="sepalWidth"
          label="Sepal Width (cm)"
          thumb-label="always"
          max="5"
          min="1"
          step="0.1"
        ></v-slider>

        <v-slider
          color="orange"
          class="mt-12"
          v-model="petalLength"
          label="Petal Length (cm)"
          thumb-label="always"
          max="10"
          min="1"
          step="0.1"
        ></v-slider>

        <v-slider
          color="green"
          class="mt-12"
          v-model="petalWidth"
          label="Petal Width (cm)"
          thumb-label="always"
          max="5"
          min="0.1"
          step="0.1"
        ></v-slider>

      </v-col>
    </v-row>

    <v-row justify="center" >
      <v-btn :loading="predictLoading" @click="predict" >Predict</v-btn>
    </v-row>

    <v-overlay :value="overlay">

      <v-row
        align="center"
        justify="center"
      >

        <v-card>
          <v-img v-show="$vuetify.breakpoint.xsOnly" max-height="300" max-width="300" :src="images[predictedClass]"></v-img>
          <v-img v-show="$vuetify.breakpoint.smAndUp" max-height="450" max-width="500" :src="images[predictedClass]"></v-img>
          <v-card-text>
            <span class="headline text--primary">
              {{predictedClass}}
            </span>
          </v-card-text>
        </v-card>

      </v-row>

      <v-row justify="center">
        <v-btn
          class="mt-4"
          @click="overlay = false;"
        >
          Close
        </v-btn>
      </v-row>

    </v-overlay>

  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',

  data: () => ({
    sepalLength: 5,
    sepalWidth: 3,
    petalLength: 5,
    petalWidth: 1,

    predictedClass: false,
    overlay: false,
    predictLoading: false,

    images:
      {
        'Virginica': 'https://www.fs.fed.us/wildflowers/beauty/iris/Blue_Flag/images/iris_virginica/iris_virginica_virginica_lg.jpg',
        'Versicolor': 'http://cdn.shopify.com/s/files/1/1402/5897/products/Iris-versicolor-01_800x.jpg?v=1545932465',
        'Setosa': 'https://www.plant-world-seeds.com/images/item_images/000/007/023/large_square/iris_baby_blue.jpg?1500653527'
      }
  }),

   methods: {
    predict () {
      this.predictLoading = true
      axios.post('https://iris-classification-backend-ze252bno3q-ez.a.run.app/predict', {
        sepal_length: this.sepalLength,
        sepal_width: this.sepalWidth,
        petal_length: this.petalLength,
        petal_width: this.petalWidth
      })
        .then((response) => {
          this.predictedClass = response.data.class
          this.overlay = true
          this.predictLoading = false
        })
    }
  }
  
};
</script>