import { mount } from '@vue/test-utils';
import CarInspection from '@views/CarInspection.vue';

describe('CarInspection', () => {
  it('displays the correct total deduction based on checked checkboxes', async () => {
    // Mount the component
    const wrapper = mount(CarInspection);

    // Find the submit button and trigger a click event
    await wrapper.find('form').trigger('submit');

    // Calculate the expected deduction based on the default values of damageDescriptions
    const expectedDeduction = wrapper.vm.calculateDeduction();

    // Find the <p> element where the total deduction is displayed
    const totalDeductionElement = wrapper.find('p');

    // Assert that the text content of the <p> element matches the expected deduction
    expect(totalDeductionElement.text()).toContain(`Total Deduction: ${expectedDeduction}`);
  });
});
