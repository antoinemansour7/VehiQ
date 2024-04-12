import { mount } from '@vue/test-utils';
import UserReport from '@/views/UserReport.vue'; // Adjust the path as per your project structure

describe('UserReport.vue', () => {
  it('submits form with correct data', async () => {
    const wrapper = mount(UserReport);
    
    // Mock console.log
    console.log = jest.fn();

    // Set form data
    await wrapper.setData({
      form: {
        title: 'Test Issue',
        text: 'This is a test issue description',
        severity: 'critical'
      }
    });

    // Trigger form submission
    await wrapper.find('form').trigger('submit.prevent');

    // Check if form submitted correctly
    expect(console.log).toHaveBeenCalledWith('Form submitted with data:', {
      title: 'Test Issue',
      text: 'This is a test issue description',
      severity: 'critical'
    });
  });
});
