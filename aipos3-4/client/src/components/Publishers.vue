<template>
  <b-container>
    <b-row>
      <first></first>
    </b-row>
    <b-row>
      <b-col col sm="10">
        <h1>Publishers</h1>
        <hr>
        <br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button class="btn btn-success btn-sm" type="button" v-b-modal.publisher-modal>
          Add Publisher
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Address</th>
            <th scope="col">Phone number</th>
            <th scope="col">Website</th>
            <th></th>
          </tr>
          </thead>
          <tbody :key="index" v-for="(publisher, index) in publishers">
          <tr>
            <td>{{ publisher.name }}</td>
            <td>{{ publisher.address }}</td>
            <td>{{ publisher.phone_num }}</td>
            <td>{{ publisher.website }}</td>
            <td>
              <div class="btn-group" role="group">
                <button
                  @click="editPublisher(publisher)"
                  class="btn btn-warning btn-sm"
                  type="button"
                  v-b-modal.publisher-update-modal>
                  Update
                </button>
                <button
                  @click="onDeletePublisher(publisher)"
                  class="btn btn-danger btn-sm"
                  type="button">
                  Delete
                </button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </b-col>
    </b-row>
    <b-modal hide-footer
             id="publisher-modal"
             ref="addPublisherModal"
             title="Add a new publisher">
      <b-form @reset="onReset" @submit="onSubmit" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        placeholder="Enter name"
                        required
                        type="text"
                        v-model="addPublisherForm.name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-address-group"
                      label="Address:"
                      label-for="form-address-input">
          <b-form-input id="form-address-input"
                        placeholder="Enter address"
                        required
                        type="text"
                        v-model="addPublisherForm.address">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-phone-num-group"
                      label="Phone number:"
                      label-for="form-phone-num-input">
          <b-form-input id="form-phone-num-input"
                        placeholder="Enter phone number"
                        required
                        type="text"
                        v-model="addPublisherForm.phone_num">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-website-group"
                      label="Website:"
                      label-for="form-website-input">
          <b-form-input id="form-website-input"
                        placeholder="Enter website"
                        required
                        type="text"
                        v-model="addPublisherForm.website">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal hide-footer
             id="publisher-update-modal"
             ref="editPublisherModal"
             title="Update">
      <b-form @reset="onResetUpdate" @submit="onSubmitUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        placeholder="Enter name"
                        required
                        type="text"
                        v-model="editPublisherForm.name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-address-edit-group"
                      label="Address:"
                      label-for="form-address-edit-input">
          <b-form-input id="form-address-edit-input"
                        placeholder="Enter address"
                        required
                        type="text"
                        v-model="editPublisherForm.address">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-phone-num-edit-group"
                      label="Phone number:"
                      label-for="form-phone-num-edit-input">
          <b-form-input id="form-phone-num-edit-input"
                        placeholder="Enter phone number"
                        required
                        type="text"
                        v-model="editPublisherForm.phone_num">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-website-edit-group"
                      label="Website:"
                      label-for="form-website-edit-input">
          <b-form-input id="form-website-edit-input"
                        placeholder="Enter website"
                        required
                        type="text"
                        v-model="editPublisherForm.website">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </b-container>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import First from './Navigation.vue';

export default {
  data() {
    return {
      publishers: [],
      addPublisherForm: {
        name: '',
        address: '',
        phone_num: '',
        website: '',
      },
      editPublisherForm: {
        id: '',
        name: '',
        address: '',
        phone_num: '',
        website: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
    first: First,
  },
  methods: {
    getPublishers() {
      const path = 'http://localhost:5000/publishers/';
      axios.get(path)
        .then((res) => {
          this.publishers = res.data.publishers;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
        });
    },
    addPublisher(payload) {
      const path = 'http://localhost:5000/publishers/add/';
      axios.post(path, payload)
        .then((res) => {
          this.getPublishers();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error);
          this.getPublishers();
        });
    },
    initForm() {
      this.addPublisherForm.name = '';
      this.addPublisherForm.address = '';
      this.addPublisherForm.phone_num = '';
      this.addPublisherForm.website = '';
      this.editPublisherForm.name = '';
      this.editPublisherForm.address = '';
      this.editPublisherForm.phone_num = '';
      this.editPublisherForm.website = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addPublisherModal.hide();
      const payload = {
        name: this.addPublisherForm.name,
        address: this.addPublisherForm.address,
        phone_num: this.addPublisherForm.phone_num,
        website: this.addPublisherForm.website,
      };
      this.addPublisher(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addPublisherModal.hide();
      this.initForm();
    },
    editPublisher(publisher) {
      this.editPublisherForm = publisher;
    },
    updatePublisher(payload, publisherID) {
      const path = `http://localhost:5000/publishers/${publisherID}/edit/`;
      axios.put(path, payload)
        .then((res) => {
          this.getPublishers();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPublishers();
        });
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editPublisherModal.hide();
      const payload = {
        name: this.editPublisherForm.name,
        address: this.editPublisherForm.address,
        phone_num: this.editPublisherForm.phone_num,
        website: this.editPublisherForm.website,
      };
      this.updatePublisher(payload, this.editPublisherForm.id);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editPublisherModal.hide();
      this.initForm();
      this.getPublishers();// why?
    },
    removePublisher(publisherID) {
      const path = `http://localhost:5000/publishers/${publisherID}/delete/`;
      axios.delete(path)
        .then((res) => {
          this.getPublishers();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPublishers();
        });
    },
    onDeletePublisher(publisher) {
      this.removePublisher(publisher.id);
    },
  },
  created() {
    this.getPublishers();
  },
};
</script>
