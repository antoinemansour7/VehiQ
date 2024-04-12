import { mount } from '@vue/test-utils';
import CSRReport from '@views/CSRReport.vue'; // Adjust the import path as per your project structure

describe('CSRReport', () => {
  it('submits the form with correct data', async () => {
    // Mount the component
    const wrapper = mount(CSRReport);

    // Set initial form data
    wrapper.setData({
      form: {
        title: 'Test Title',
        text: 'Test Description',
        severity: 'critical'
      }
    });

    // Trigger form submission
    wrapper.find('form').trigger('submit.prevent');

    // Wait for next tick to allow the promise chain to be resolved
    await wrapper.vm.$nextTick();

    // Check if form data is reset after submission
    expect(wrapper.vm.form.title).toBe('');
    expect(wrapper.vm.form.text).toBe('');
    expect(wrapper.vm.form.severity).toBe('critical');

    // Unmount the component
    wrapper.destroy();
  });
});
