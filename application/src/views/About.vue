<template>

    <v-container>
      <v-row justify="center">
        <v-col md="6" class="pa-4">

          <v-card class="mb-4 mt-2" raised="true">
            <v-card-title>About</v-card-title>
            <v-card-text>
              This is a simple web application to classify irises as virginica, versicolor or setosa.
              We need 4 features to achive this task.
              These features are sepal length, sepal width, petal length and petal width.
              This application lets you fiddle with these features and see the prediction of a deep neural network for the values you pick.
            </v-card-text>
          </v-card>

          <v-card class="my-4" raised="true">
            <v-card-title>Source Code</v-card-title>
            <v-card-text>
              You can view the source code of this project on Github.
              <br>
              <v-btn outlined href="https://github.com/metesengul/iris-classifier" class="mt-2">Github</v-btn>
            </v-card-text>
          </v-card>

          <v-card class="my-4" raised="true">
            <v-card-title>Developer</v-card-title>
            <v-card-text>
              This app is created by Mete Şengül. For more information you can visit my website.<br>
              <v-btn outlined href="https://metesengul.com" class="mt-2">Website</v-btn>
            </v-card-text>
          </v-card>

        </v-col>
      </v-row>

    </v-container>

</template>

<script>

export default {

  data: () => ({

  })

}
</script>
