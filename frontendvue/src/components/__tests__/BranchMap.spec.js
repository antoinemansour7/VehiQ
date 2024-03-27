import { mount } from "@vue/test-utils";
import BranchMap from "@/components/BranchMap.vue";
import axios from "axios";
import MockAdapter from "axios-mock-adapter";

describe("BranchMap.vue", () => {
  it("fetches branches and renders them", async () => {
    const mock = new MockAdapter(axios);
    const branches = [
      {
        id: 1,
        name: "Branch 1",
        location: { coordinates: [-122.084, 37.422] },
      },
    ];
    mock.onGet("http://localhost:8000/branches/").reply(200, branches);
    const wrapper = mount(BranchMap);
    await wrapper.vm.$nextTick(); // Wait for promise resolution
    expect(wrapper.vm.branches).toEqual(branches);
  });
});
