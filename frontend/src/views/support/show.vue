<template>
    <div>

        <v-layout row wrap class="formBox">
            <div class="bgPhoto">
                <img src="../../../public/images/contact-us-concept-landing-page_52683-12759.svg" class="supportPhoto">
            </div>

            <v-flex xs12 md12>
                <div class="userDetails">
                    <h3 class="title">Need support ? </h3>
                </div>
            </v-flex>

            <v-flex xs12 md12 class="introSupport">

                <br>

                <h3>We'd love to talk about how we can work together</h3>
                <p>We are not “yes-people” that code upon your guidelines - we question, discuss, advise. Simply, we
                    make the difference.</p>
                <strong>Agree !!! Then send us a message</strong>

            </v-flex>

            <v-flex xs12 md2></v-flex>

            <v-flex xs12 md4>

                <div class="mditSupport">
                    <h3 class="supportTitle">
                        <i class="mdi mdi-star"></i>
                        MicroDreamIT
                    </h3>

                    <p>
                        Level 5, Sheikh Hasina Software Technology Park Jashore, Bangladesh
                    </p>
                    <ul class="contactList">
                        <li><i class="mdi mdi-whatsapp"></i> +8801763759009</li>
                        <li><i class="mdi mdi-cellphone-iphone"></i>Phone +88-01976-062011</li>
                        <li><i class="mdi mdi-skype"></i>shahanur.sharif84</li>
                        <li><i class="mdi mdi-email-open"></i>shahanur700@gmail.com</li>
                    </ul>
                </div>

            </v-flex>

            <v-flex xs12 md4>
                <div class="mditSupport">
                    <h3 class="supportTitle">
                        <i class="mdi mdi-star"></i>
                        OtherCompany
                    </h3>

                    <p>
                        Ohter Compnay title will be here !
                    </p>
                    <ul class="contactList">
                        <li><i class="mdi mdi-whatsapp"></i> +8801763759009</li>
                        <li><i class="mdi mdi-cellphone-iphone"></i>Phone +88-01976-062011</li>
                        <li><i class="mdi mdi-skype"></i>shahanur.sharif84</li>
                    </ul>
                </div>

            </v-flex>

            <v-flex xs12 md2></v-flex>
            <v-flex xs12 md12 class="py-12">

            </v-flex>


        </v-layout>
    </div>
</template>

<script>
    export default {
        name: "show.vue"
    }
</script>

<style scoped lang="scss">

    .formBox {
        padding: 20px;
        overflow: hidden;
        .bgPhoto {
            position: absolute;
            z-index: -1;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            background: aliceblue;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    }


</style>