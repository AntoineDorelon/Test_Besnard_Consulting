import { mount } from "@vue/test-utils";
import ValueItem from "../../src/components/ValueItem";

describe("ValueItem", () => {
  const value = { id: 1, title: "test-value" };
  const wrapper = mount(ValueItem, {
    propsData: { value },
  });

  test("contains value title in 'Camel case' when a value is passed", () => {
    expect(wrapper.html()).toContain(
      value.title.charAt(0).toUpperCase() + value.title.slice(1)
    );
  });

  it("emits event 'ValueDelete' when we click on the trash icon", async () => {
    const trashicon = wrapper.find(".trash");
    await trashicon.trigger("click");
    //assert event is called
    expect(wrapper.emitted().ValueDelete).toBeTruthy();
    //assert we pass an array of 2 fields
    expect(wrapper.emitted().ValueDelete.length).toBe(1);
    //expect we pass the right id
    expect(wrapper.emitted().ValueDelete[0]).toEqual([1]);
  });

  it("emits event 'ValueEdit' when we click on the edit icon", async () => {
    const editicon = wrapper.find(".edit");
    await editicon.trigger("click");
    //assert event is called
    expect(wrapper.emitted().ValueEdit).toBeTruthy();
    //assert we pass an array of 2 fields
    expect(wrapper.emitted().ValueEdit.length).toBe(1);
    //expect we pass the right id
    expect(wrapper.emitted().ValueEdit[0]).toEqual([1]);
  });
});
